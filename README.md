# The Andro Experiment

Hello! This is a CTF challenge I made for the RITSEC CTF 2024. 

###### (Based off a challenge I made for a different competition)

This is one of the 4 challenges I made for the CTF, if there's interest I can upload the other 3.

### Challenge Description:
```yml
Name: The Andro Experiment
Difficulty: Medium/Hard
Type: Reversing

Definition:
Hey, it's Chase again. I did some more research into some of the experiments Anthony was doing and found this(http://the-andro-experiment.ctf.ritsec.club) website.
Something about an android application calling back to a server, so once again see if there is any information on the server about him?
```

Repo is described as

- Andro (the APK file)
- challenge (the entire challenge to host)
- healthcheck (challenge healthcheck for [kCTF](https://google.github.io/kctf/))
- writeup (the writeup and solution scripts)
- chal.txt (challenge description)
- challenge.yaml ([kCTF](https://google.github.io/kctf/) configuration file)
- README.md (this lol)
- LICENSE (MIT License)

The original hosting for the challenge is offline, but I edited the challenge so you can self host it! 

Docker selfhosting steps:

```shell
cd challenge
sudo docker compose up --build
```

Then access the challenge at [localhost:5000](https://127.0.0.1:5000)

Try to figure it out yourself before you look at the writeup!!!
