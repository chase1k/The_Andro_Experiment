Java.perform(function() {

    Java.choose("com.example.andro.MainActivity", {
        onMatch(main_instance){
          console.log("seed: " + main_instance.seed.value);
        },
        onComplete(){
          console.log("Dawg, what happened");
        }
       })


});