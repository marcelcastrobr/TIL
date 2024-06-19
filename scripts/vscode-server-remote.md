# Visual Studio Code using your Browser

Do you need to quickly open a development environent to test something. 

Check vscode-server. This might be helpfull for you that do not have ssh port open or would like to use your tablet.

In this steps I am using an EC2 amazon-linux-3 t2.micro.

**Step 1: Access your instance**

After launching the ec2, simply try to connect to it via "EC2 instance connect".

![image-20230324093835197](/Users/marcasbr/Library/Application Support/typora-user-images/image-20230324093835197.png)



**Step 2: Install vscode-server**

```bash
# install vscode-server
wget -O- https://aka.ms/install-vscode-server/setup.sh | sh 
```

You will get a use code that you use to authenticate to https://github.com/login/device.

After that, vscode-server create a tunnel to your machine and provide you a link like:

https://insiders.vscode.dev/+ms-vscode.remote-server/<name-of-set-to-your-machine>



**Step 3: Enjoy vscode-server**

Open your web browser of choice (I used chrome) and access the link.



