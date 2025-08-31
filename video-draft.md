# Video draft

Hello, tutor.

Now I will show you my approach and methods for challenges that I found interesting and learned something from them.

First is Leviathan level 6. I came up with two methods to crack it. The first is brute force cracking, and the second is using gdb for reverse analysis.

(run the leviathan6)

After logging in, I first checked what was in the home directory. I found an executable file called leviathan6. Let's run it and see what happens.

(run `ltrace ./leviathan6`)

As you can see, it outputs a prompt says that use it with a 4 digit code. So let's try to use it with 1234. Then we got a wrong. I tried to find something with ltrace command. But I still couldn't find any useful information.

(open brute.sh)

So I tried to brute force it. And this is my script.

(show the shell and whoami and cat password)

After running for about 5 seconds, I got the shell. Type the whoami command. It's leviathan 7. Then I can get the password.

It is easy. However, after completing several Narnia challenges, I gained some knowledges of reverse engineering. Therefore, I wondered if I could use reverse engineering here to analyze what the password is.

(gdb disass main)

So I use gdb to disassemble the programme. Then I found a jump operation. There is a comparison before this jump, which is most likely comparing the password with the value I entered.

(run with 0000)

As for which register, eax or ebp, contains the address I want, I can check the data stored in registers by running the program with 0000.

(check registers)

Let's check the registers. I found that the data stored in eax was 0. This means that the address ebp minus c stores the password I want.

(check data)

Let's see what's there. 7123. This result is the same as the number we obtained through brute force.

Then I want to show you Narnia level 1. This one isn't difficult, but I got stuck here for several days because of one problem.

(ls -al)

All relevant code for this section is located in the narnia folder. Here you can see the source code and executable files for each level. Let's run it and see what happens.

(run narnia1)

This output seems to hint that I should initialize an environment variable named EGG. Let’s have a look at the source code.

(cat narnia.c)

You can see that the code will execute anything I put in the EGG. So if I put a shellcode that can run a interactive shell, I can maybe get the password.

(execve("/bin/sh"))

I chose a shellcode from internet. It run this command execve("/bin/sh").

(export EGG="...")

(run narnia1)

Let's see what'll happen. I can get the shell by setting EGG to this shellcode. But when I type whoami command, it told me that the current user is still narnia1. In this case, I couldn't get the password for narnia2. So what's the problem?

After searching online, I realized that this was due to a permission inheritance issue. In Linux programs, there are concepts of euid and ruid. Ruid is the real UID of the user who started the process. It represents the actual owner of the process. Euid is the process's current effective UID. It determines the access privileges that the process has when performing operations such as opening files and creating processes.

When a process executes a program file with the setuid bit set, the euid of the new process is set to the UID of the file owner. So I use ls dash l command to check this.

(ls -al)

As you can see, the executable file has the setuid bit set. Therefore, the problem does not lie here.

After being stuck for several days, I suddenly realized that although narnia1 had setuid, the shellcode was not a file and did not set the uid when running the shell. Therefore, when the programme ran the shellcode, the euid reverted to ruid without the setuid bit set. I needed to add a setreuid function before running the shell command to set the uid, allowing user narnia2 to run the shell instead of narnia1.

(export EGG="...")

So I will use this shellcode to do it.

(input "setreuid(get)...")

The command it runs looks like this.

Let's try to run again.

(run narnia2, whoami, password)

Alright. The current user has become narnia2. Then I can get the password.

All my writeups have been uploaded to Github. This is the link to my Github page.

Thanks for your watching.
