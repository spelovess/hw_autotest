#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import config


def test_attacker_add_report():
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=config.localhost, port=config.port, username=config.user, password=config.passwd)
    # stdin,stdout,stderr=s.exec_command('/root/test.sh')
    stdin, stdout, stderr = s.exec_command('cd gongfangautotest/chengsheng;'
                                           'python 07_new_admin_add_report_attack_strategy_1judge.py')
    out = stdout.readlines()
    print(out)
    check = ['登陆成功\n', '工具值传入错误，返回结果验证成功\n', '工具值不存在时，返回结果验证成功\n',
             '提交攻击队伍成绩成功\n']
    assert out == check
    s.close()