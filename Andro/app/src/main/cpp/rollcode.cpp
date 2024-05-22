#include <jni.h>
#include <stdio.h>
#include <dlfcn.h>
#include <malloc.h>
#include <string.h>
#include <string>
#include <jni.h>
#include <android/log.h>
#include <cstdio>
#include <openssl/rand.h>
#include <openssl/sha.h>

// Roll code function
char* rollCode(const char* seed, size_t size) {

    char* buffer = static_cast<char *>(malloc(32));
    __android_log_print(ANDROID_LOG_DEBUG, "rollcode", "C Hash: %x %x %x %x\n", seed[0], seed[1], seed[2], seed[3]);

    SHA256(reinterpret_cast<const unsigned char *>(seed), size,
           reinterpret_cast<unsigned char *>(buffer));

    return buffer;
}

extern "C"
JNIEXPORT jbyteArray JNICALL
Java_com_example_andro_MainActivity_rollCode(JNIEnv *env, jobject thiz, jbyteArray jseed) {

        jboolean booler = true;
        char* seeed = reinterpret_cast<char *>(env->GetByteArrayElements(jseed, &booler));
        char* hashedSeed = rollCode(seeed, (size_t)env->GetArrayLength(jseed));

        jbyteArray ret_array = env->NewByteArray(32);
        env->SetByteArrayRegion(ret_array, 0, 32, reinterpret_cast<const jbyte *>(hashedSeed));

        free(hashedSeed);
        return ret_array;
}

int generateSeed(){

    FILE *urandom = fopen("/dev/urandom", "rb");
    if (urandom == nullptr) {
        perror("Error opening /dev/urandom");
        return 0;
    }

    unsigned int buffer;
    size_t bytesRead = fread((void *)(&buffer), sizeof(unsigned char), 4, urandom);
    if (bytesRead != 4) {
        perror("Error reading from /dev/urandom");
        fclose(urandom);
        return 0;
    }

    fclose(urandom);
    return buffer;
}

extern "C" jbyteArray
Java_com_example_andro_MainActivity_generateSeed(JNIEnv * env, jobject
thiz) {

    int iseed = generateSeed();
    jbyteArray ret_array = env->NewByteArray(4);
    env->SetByteArrayRegion(ret_array, 0, 4, reinterpret_cast<const jbyte *>(&iseed));
    return ret_array;

}
__attribute__((used))
void command_server(char* command){
    char buf[4096];
    snprintf(buf, sizeof(buf), "/experiment?command=%s", command);
    perror("UNIMPLEMENTED");
    perror("Server expects okhttp");
    abort();

}


