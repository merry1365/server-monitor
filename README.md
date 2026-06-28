# server-monitor

Sakura VPS上で動作する簡易サーバー監視ツールです。

## 概要

PythonでホストサーバーのCPU・メモリ・ディスク使用率を1秒ごとに取得し、Nginxで公開するHTMLファイルに出力します。  
Pythonスクリプトはsystemdサービスとして常駐起動しています。

## 使用技術

- Ubuntu
- Python
- psutil
- systemd
- Nginx
- Git / GitHub

## 実装内容

- CPU使用率の取得
- メモリ使用率の取得
- ディスク使用率の取得
- 閾値を超えた場合にWARNING表示
- Nginx経由でWeb公開
- systemdによる常駐化

## 技術選定

常時監視を行いたかったため、cronではなくsystemdでPythonスクリプトをサービス化しました。  
systemctlで状態確認・起動・停止ができ、journalctlでログ確認できる点を重視しました。

## 動作環境

- Ubuntu 26.04
- Python 3.12

## 環境変数

例として`.env` に以下を設定します。

```env
OUTPUT_FILE=/var/www/html/index.html
CPU_LIMIT=80
MEMORY_LIMIT=90
DISK_LIMIT=85
