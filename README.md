# deployd
持续部署的文件分发和远程命令工具

### 安装
1. `cd /mnt`
2. `git clone https://github.com/qorzj/deployd.git`
3. `pip install -r deployd/requirements.txt`
4. `cp deployd/init.d-deployd /etc/init.d/deployd`
5. `chmod +x /etc/init.d/deployd`

### 启动
`service deployd start`

### 停止
`service deployd stop`

### 卸载
`rm /etc/init.d/deployd`

### 示例
client端的命令： `curl -F "data=@{local_file_path}" -F "cmd={deploy_command}" -H "token: {token}"  http://{host}:{port}{server_working_dir}`

server端的设置:  
`cat {server_working_dir}/.deployd.conf`
```
{client_ip1}  {token1}
{client_ip2}  {token2}
...
```
