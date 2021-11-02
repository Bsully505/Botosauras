const {spawn} = require('child_process');
//To See Python Version
    //const childPython = spawn('python', ['--version']);
//To Run Entire Code
    const childPython = spawn('python',['DiceRoller.py']);
//TO Run Entire Code With Argument
    //const childPython = spawn('python',['DiceRoller.py' , 'ENTER ARGUMENT HERE']);

childPython.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
});

childPython.stderr.on('data',(data) =>{
    console.error(`stderr: ${data}`);
});
//In case nothing happens
childPython.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});