package com.example.andro;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

import com.example.andro.R;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {
    static byte[] seed = new byte[0];
    ExecutorService executor = Executors.newFixedThreadPool(10);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        System.loadLibrary("andro");
        System.loadLibrary("ssl");
        System.loadLibrary("crypto");

        seed = generateSeed();
        performGetRequest();
        Button myButton = findViewById(R.id.button);

        myButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("rollcode", "OnClick" + Arrays.toString(seed));
                seed = rollCode(seed);
                sendBytesToServer(seed);
            }
        });
    }
    public native byte[] rollCode(byte[] seed);
    public native byte[] generateSeed();

    private void sendBytesToServer(byte[] code) {

        executor.execute(new Runnable() {
            @Override
            public void run() {

                final MediaType RAW = MediaType.get("application/octet-stream");

                OkHttpClient client = new OkHttpClient();
                String url = "http://10.0.2.2:5000/ping";

                RequestBody body = RequestBody.create(code, RAW);
                Request request = new Request.Builder()
                        .url(url)
                        .post(body)
                        .build();

                try (Response response = client.newCall(request).execute()) {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            // Handle the response here, such as updating UI or processing data
                            if (code[0] != 'S') {
                                Toast.makeText(MainActivity.this, "Ping Sent", Toast.LENGTH_SHORT).show();
                            } else {
                                Toast.makeText(MainActivity.this, "Server Authenticated", Toast.LENGTH_SHORT).show();
                            }
                        }
                    });
                } catch (IOException e) {
                    Log.d("MainErr", e.toString());
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            // Handle error, such as displaying a message to the user
                            Toast.makeText(MainActivity.this, "Could Not Send", Toast.LENGTH_SHORT).show();

                        }
                    });
                }
            }
        });

    }

    private void performGetRequest() {
        String seed_marker = "SEED:";
        byte[] result = new byte[seed_marker.length() + 4];
        for(int i = 0; i< seed_marker.length(); i++){
            result[i] = seed_marker.getBytes()[i];
        }

        for(int i = 0; i<seed.length; i++){
            result[i+ seed_marker.length()] = seed[i];
        }
//        Log.d("rollcode", Arrays.toString(seed));
        sendBytesToServer(result);
    }


}