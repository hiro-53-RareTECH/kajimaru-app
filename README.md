# ✨ かじまる
プロジェクト名の由来は、「家事 ＋ まるっと」であり、日々の家事を全部回す・まるく収めることをねらいとする。

## 📚 目次
- [プロジェクト概要](#プロジェクト概要)
- [自分の担当](#自分の担当)
- [背景](#背景)
- [ターゲット](#ターゲット)
- [使用技術](#使用技術)
- [技術選定理由](#技術選定理由)
- [スタート画面、ダッシュボード画面](#スタート画面ダッシュボード画面)
- [機能一覧](#機能一覧)
- [ディレクトリ・ファイル構成](#ディレクトリファイル構成)
- [開発環境確認手順](#開発環境確認手順)
- [インフラ設計の詳細](#インフラ設計の詳細)

## プロジェクト概要
- 開発体系：チーム開発（ハッカソン）
- 制作期間：2ヶ月
- メンバー：4名（フロントエンド1名、バックエンド2名、インフラ1名）

## 自分の担当
「インフラ」担当として、ディレクトリ・ファイルの構成検討、Dockerによる開発環境構築、ドメイン取得、AWSによる本番環境のデプロイを行った。

## 背景
家庭やパートナーを持つと「家事の分担をどうするか」という問題が必ず生じると考えた。  
「家事の偏り」、「公平感の欠如」、「家事へのモチベーション維持」といった課題を解決するために、円滑に家事を回し、家族間のコミュニケーションを活発化するためのアプリを開発することとした。

## ターゲット
- 家事の偏りがあり不満を感じている人
- 子供に家事をさせたいが、継続できずに困っている親
- 家事を通じて家庭内のコミュニケーションを活発化させたい家庭

## 使用技術
<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/2114c333-c040-4f7d-abb7-367f349c0fd0" />

| **カテゴリ** | **技術** |
| --- | --- |
| フロントエンド | HTML / CSS / JavaScript / Bootstrap 25.2 |
| バックエンド | Python 3.13 / Django 5.2.7 / MySQL 8.4 |
| インフラ | Docker / AWS / Gunicorn 23.0.0 / NGINX 1.28 |
| その他 | ovice / Mattermost / [draw.io](http://draw.io) / Canva / Figma / GitHub |

## 技術選定理由
<details>
    <summary>フロントエンド</summary>

**1) JavaScript** <br>
React, VueといったJavaScriptのライブラリは、開発メンバーの知見がないことおよび2ヶ月間という限られた期間内では学習コストが高いため、素のJavaScript（Vanila JS）を採用することとした。

**2) Bootstrap** <br>
開発スピードの向上を図るため、HTMLのクラスの中でCSSを記述できるBootstrapを採用した。<br>
PythonのパッケージにDjangoの中で使用できる「django-bootstrap5」があるため、これを採用した。<br>

</details>

<details>
    <summary>バックエンド</summary>

**1) Python** <br>
開発メンバーの共通学習言語が「Python」であり、チーム開発を通じてさらにPythonの知識・経験を身につけるため「Python」を選定した。
PythonのバージョンはDjangoとの互換性を考慮して、2025年10月時点での最新バージョンである「3.13」とした。
DjangoとPythonのバージョン互換性は以下の公式ドキュメントに記載があり、その中の「DjangoでどのPythonのバージョンを使用すべきですか」についての回答より、「新しいバージョンのPythonはより高速で、多くの機能があり、サポートされているので、Python 3 の中でも最新バージョンを推奨します」との記載がある。
よって、開発スタート時の2025年10月時点での最新バージョンであるPython「3.13」を採用した。

参考URL
https://docs.djangoproject.com/ja/5.2/faq/install/

**2) Django** <br>
Pythonのフレームワークとして、フルスタックである「Django」を採用した。
チーム開発メンバーは「Flask」の経験があるものの、「Django」を使用して開発を行うことは初めてであったため、学習目的から「Django」を採用した。
Djangoのバージョンは、2025年10月時点でのLTS（Long Term Support：長期間安定サポート）である「5.2.7」を採用した。

**3) MySQL** <br>
MySQL、PostgreSQL、Sqliteの3つのデータベースを比較検討し、WEBアプリ開発の定番であり、リソース消費量、学習コストがを小さい「MySQL」を採用することとした。
以下にデータベースの比較表を示す。

| **選択肢** | **メリット** | **デメリット** | **活用事例** | **採用** |
| --- | --- | --- | --- | --- |
| MySQL | ・高速で読み取りが可能<br>・豊富なドキュメント情報がある<br>・運用がしやすい | ・複雑なクエリ処理ではPostgreSQLに劣る<br>・ライセンス料が発生する可能性がある | **1) 主な用途**<br>・Webアプリ<br>・中規模アプリ（1万～10万ユーザー）<br><br>**2) 接続数 / メモリ消費量**<br>・数千の同時接続<br>・100～500MB | ◯ |
| PostgreSQL | ・高機能かつ拡張性が高い<br>・豊富なデータ型<br>・複雑なクエリ処理に強い<br>・ACID準拠で堅牢性が高い | ・リソース消費量が大きめ<br>・設定が複雑で学習コストが高い | **1) 主な用途**<br>・ビジネスアプリ<br>・金融システム<br>・大規模アプリ（10万ユーザー以上）<br><br>**2) 接続数 / メモリ消費量**<br>・数万の同時接続<br>・200MB～1GB | △ |
| SQLite | ・インストール不要ですぐ使用可能<br>・単一ファイルで軽量<br>・プロトタイプに最適<br>・サーバー不要 | ・同時書き込みが苦手<br>・大容量データに不向き<br>・冗長化が難しい | **1) 主な用途**<br>・モバイルアプリ<br>・組み込みシステム<br>・小規模アプリ（〜1万ユーザー）<br><br>**2) 接続数 / メモリ消費量**<br>・単一プロセスのみ<br>・〜10MB | △ |



</details>

<details>
    <summary>インフラ</summary>
インフラ構造は、Web3層構造（Webサーバー、アプリケーションサーバー、データベースサーバー）とした。<br>
各層を独立させることで、「開発性・保守性」を向上させるものとした。<br>
また、自身がインフラ構築を初めて行うため、学習目的も兼ねて基本的なWeb3層構造を実装することとした。<br>

**1) AWS** <br>
AWSの技術選定理由は「[インフラ設計の詳細](#インフラ設計の詳細)」で述べる。          

**2) Gunicorn** <br>


**3) NGINX** <br>
    
</details>

## スタート画面、ダッシュボード画面
### スタート画面
<table>
<tr>
<td><img src="https://github.com/user-attachments/assets/faca24c0-602e-425c-afd6-3e559d939498" width="100%"></td>
<td><img src="https://github.com/user-attachments/assets/bbdec27b-b366-442c-9285-4933ad764c92" width="100%"></td>
<td><img src="https://github.com/user-attachments/assets/bb4cf3c8-5e5b-4255-9903-517a5993662c" width="100%"></td>
</tr>
</table>
    
### ダッシュボード画面
<table>
<tr>
<td><img src="https://github.com/user-attachments/assets/70ff15cc-f40a-4119-8de0-a57d836a9795" width="100%"></td>
<td><img src="https://github.com/user-attachments/assets/b5c876e4-c6af-4c4d-a37f-9db573425092" width="100%"></td>
<td><img src="https://github.com/user-attachments/assets/1108cffb-6776-465a-85fe-7eec9c2e4b34" width="100%"></td>
</tr>
</table>

## 機能一覧
<details>
<summary>MVP機能</summary>

| **カテゴリ** | **MVP機能** | **進捗** |
| --- | --- | --- |
| **登録画面** | 新規ユーザー登録(管理者のみ) | ◯ |
|  | 初期プロフィール作成 | ◯ |
|  | ログイン | ◯ |
|  | 参加コード（８桁）の発行 | ◯ |
|  | 招待コード入力画面 | ◯ |
| **ユーザー管理** | 共通端末ホーム | ◯ |
|  | 一般ユーザーのログイン | ◯ |
|  | 自身のマイページにログイン | ◯ |
|  | ログアウト | ◯ |
|  | セッションログアウト | ◯ |
|  | 一般ユーザー管理 | ◯ |
|  | タイムアウト | ◯ |
| **家事の自動ローテーション** | ローテ単位 | ◯ |
|  | タスクリストの作成 | ◯ |
|  | 各タスクの重み付け | ◯ |
|  | タスクリストから自動割当 | ◯ |
|  | 多忙フラグで自動回避 | ◯ |
| **ダッシュボード（ホーム画面）** | タスクの担当を表示 | ◯ |
|  | タスクの達成率を表示 | ◯ |
|  | 未着手家事表示 | ◯ |
|  | 割当重みづけ | ◯ |
| **通知** | 前夜/当日朝に担当者へ通知 | ◯ |
|  | 遅延の通知 | ◯ |
|  | チャンネル | ◯ |
|  | 担当表の通知 | ◯ |

</details>

<details>
<summary>追加機能</summary>

| **カテゴリ** | **追加機能** | **進捗** |
| --- | --- | --- |
| **買い物リスト** | アイテム/数量/メモ/カテゴリ管理 | ◯ |
|  | チェックボックスの設置 | ◯ |
|  | アイテムの追加 | ◯ |
|  | リストへ追加は承認を付ける | ◯ |
|  | 履歴の保管 | ◯ |
| **代役マッチング** | 代役リクエスト | ◯ |
|  | ワンタップ承認 | ◯ |
|  | 承認者に自動再配分 | ◯ |
|  | 履歴を保存 | ◯ |
| **家電・設備メンテ台帳** | 機器ごとに最終実施日/推奨実施日/月齢カウンタ | ◯ |
|  | 期限で自動でタスクに追加 | ◯ |
| **在庫ハブ** | 品目/単位/期間/最低在庫管理 | ◯ |
|  | ワンタップ減算 | ✕ |
|  | 低下時に「買い物リストに追加」 | ◯ |
| **天気×家事レコメンド** | 天気を取得 | ◯ |
|  | 天気と照合し今日のおすすめを提示 | ◯ |

</details>

## ディレクトリ・ファイル構成
<details>
<summary>ディレクトリ・ファイル構成</summary>
本プロジェクトのディレクトリ・ファイル構成を以下のとおり示す。

<pre>
.
└── kajimaru-app/
    ├── .github/
    │   └── workflows/
    │       ├── NotifyMEGE.yml
    │       └── NotifyPR.yml
    ├── docker/
    │   ├── django_cron
    │   ├── Dockerfile
    │   ├── Dockerfile.prod
    │   └── wait-for-it.sh
    ├── infra/
    │   └── nginx/
    │       ├── conf.d/
    │       │   └── kajimaru.conf
    │       ├── Dockerfile
    │       └── nginx.conf
    ├── src/
    │   ├── apps/
    │   │   ├── dashboard
    │   │   ├── maintenance
    │   │   ├── notification
    │   │   ├── rotation
    │   │   ├── shopping
    │   │   ├── stocks
    │   │   ├── user
    │   │   └── weather
    │   ├── config/
    │   │   ├── settings/
    │   │   │   ├── base.py
    │   │   │   ├── dev.py
    │   │   │   └── prod.py
    │   │   ├── asgi.py
    │   │   ├── urls.py
    │   │   ├── views.py
    │   │   └── wsgi.py
    │   ├── static/
    │   │   ├── css
    │   │   ├── img
    │   │   └── js
    │   ├── templates/
    │   │   ├── components
    │   │   ├── dashboard
    │   │   ├── maintenance
    │   │   ├── rotation
    │   │   ├── shopping
    │   │   ├── stocks
    │   │   ├── user
    │   │   └── base.html
    │   └── manage.py
    ├── staticfiles
    ├── .dockerignore
    ├── .env
    ├── .envexample
    ├── .gitignore
    ├── docker-compose.prod.yml
    ├── docerk-compose.yml
    ├── Makefile
    ├── README.md
    └── requirements.txt
</pre>
</details>

## 開発環境確認手順
<details>
<summary>Dockerの起動から終了までの手順</summary>

### 1) 環境変数ファイル.envの作成
.env.exampleをコピーして、.envファイルをプロジェクトルートディレクトリ直下に保存する。  
注）.envファイルは必ず、.env.exampleファイルと同じ階層に保存すること。（Docker、Djangoの設定ファイルで環境変数.envのファイルパスを指定しているため。）  
```
cp .env.example .env
```

以下が.env.exampleの中身であり、「各自で変更する設定」を各自で変更する。  
「DJANGO_SECRET_KEY」の設定は、以下のとおりである。  
```
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

```
# ======= ✅ チームで共通にする設定 =======
MYSQL_DATABASE=django_db                    # 開発環境で使うデータベース名（チームで共通・固定）
MYSQL_USER=dev_user                         # 開発用のデータベースユーザ名（チーム共通）
MYSQL_HOST=db                               # Django(web)コンテナが接続するDBコンテナ名(db)（チーム共通）
DJANGO_PORT=8000                            # Djangoのポート番号（チーム共通）
DJANGO_LANGUAGE_CODE=ja                     # 言語コード設定(チーム共通)
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1    # アプリにアクセスできるホスト・ドメイン名（チーム共通）
DJANGO_SETTINGS_MODULE=config.settings.dev  # 開発環境ファイルの参照（チーム共通）
TZ=Asia/Tokyo                               # タイムゾーン設定（チーム共通）
USERNAME=appuser                            # コンテナ内のユーザーネーム（チーム共通）
GROUPNAME=appgroup                          # コンテナ内のグループネーム（チーム共通）

# ======= 🔧 各自で変更する設定 =======
MYSQL_PASSWORD=your_own_password            # 各自がローカル環境で設定するDBユーザーパスワード(環境開発で各自設定、非公開)
MYSQL_ROOT_PASSWORD=your_root_pw            # MYSQLのrootパスワード(開発環境で各自設定、非公開)
DJANGO_SECRET_KEY=your_secret_key           # Djangoのセキュリティキー(必ず各自で生成すること)
DJANGO_DEBUG=True                           # デバッグモード設定。開発中はTrue、本番や検証環境はFalse推奨
UID=your_uid                                # 各自のuidを指定（id -uコマンドで確認）
GID=your_gid                                # 各自のgidを指定（id -gコマンドで確認）
```

### 2) 起動時のdockerコマンド
初回起動ではイメージをビルドする必要があるため、以下のコマンドで起動させる。  
```
docker compose up --build
```  
もしくは  
```
make build
```  

※Makefileには、使用頻度の高いコマンドを省略して打てるように設定している。以降も通常版とmake版で記述する。

2回目以降は既にイメージがビルドされているため、以下のコマンドで起動してもよい。  
必要に応じて、 **-d** をupの後に付けて、バックグラウンドで起動してもよい。  
```
docker compose up -d
```  
もしくは  
```
make up
```

### 3) 終了時のdockerコマンド
終了時は以下のコマンドで終了する。  
必要に応じて、ボリューム（db_data）を削除する場合は、 **-v** をdownのあとに付ける。  
```
docker compose down
```  
もしくは  
```
make down
```
</details>

<details>
<summary>アクセス先</summary>
    
ブラウザで以下のアドレスを入力して、Djangoの初期画面が開いていることを確認する。  
```
http://localhost:8000/
```  
もしくは  
```
http://127.0.0.1:8000/
```  

ドキュメントが **「日本語」** 、DEBUGが **「True」** になっていることを確認する。  
成功すると以下の画面が表示される。  
<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/15fc92ec-35fb-4c9e-9c9a-3439b8e3fd29" />
</details>

<details>
<summary>各コンテナへのアクセス手順</summary>
    
### 1)MySQL(db)
MySQLコンテナへのアクセスは、以下のコマンドを入力する。  
```
docker compose exec -it db mysql -u dev_user -p
```  
もしくは  
```
make db
```  
コマンド入力後にパスワードを聞かれるため、.envの「MYSQL_PASSWORD」で設定したパスワードを各自入力する。  

### 2)Django(web)
Djangコンテナへのアクセスは、以下のコマンドを入力する。  
```
docker compose exec -it web /bin/bash
```  
もしくは  
```
make sh
```  

また、docker compose up -dで起動した後に、Djangoのlogsを確認したい場合は、以下のコマンドを入力する。  
```
docker compose logs -f web
```  
もしくは  
```
make logs
```  
</details>

<details>
<summary>Django 新規アプリ作成手順</summary>
    
### 1) 新規アプリの作成
以下のコマンドで新規アプリを作成する。  
通常のコマンドでは、長くなるため、以下のmakeコマンドを推奨する。  
<アプリ名>に作成したいアプリを入力する。  
```
make app name=<アプリ名>
```  
もしくは  
```
docker compose exec web mkdir -p apps/<アプリ名>
```  
```
docker compose exec web python manage.py startapp <アプリ名> apps/<アプリ名>
```  

コマンド入力後に、/src/appsの直下に指定したアプリが作成されていることを確認する。  

### 2) INSTALLED_APPSへの新規アプリ追加
以下のファイル（base.py）のINSTALLED_APPS変数へ新規アプリを追加する。  
```
/src/config/settings/base.py
```  
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '（ここにアプリを追加する。以下はアプリ名「test」の一例）',
    'apps.test.apps.TestConfig'
]
```

### 3) apps.pyへのname追加
新規作成したアプリディレクトリ内のapps.pyへnameを追加する。  
以下はアプリ名「test」とした場合の一例である。  
appsディレクトリ下にあるため、name=apps.<アプリ名>とする。  
```
class TestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.test'
```
</details>

<details>
<summary>Django マイグレーションファイル作成、マイグレーションの手順</summary>
    
### 1) models.pyへのテーブル定義
該当アプリディレクトリのmodels.pyにテーブルを定義する。  

### 2) マイグレーションファイルの作成
models.pyのテーブル定義後、マイグレーションファイルを作成するために以下のコマンドを入力する。  
```
docker compose exec web python manage.py makemigrations
```  
もしくは  
```
make mm
```  
マイグレーションファイルが作成されると、該当ディレクトリの「migrations」にマイグレーションファイルが作成される。（例：0001_initial.py）  

### 3) マイグレーション（データベースへの反映）
マイグレーションファイルが作成された後に、以下のコマンドを入力して、データベースへ反映させる。  
```
docker compose exec web python manage.py migrate
```  
もしくは  
```
make migrate
```  

コマンド入力後に、MySQLコンテナへ入り、テーブルが作成されていれば、マイグレーション完了である。  
</details>

<details>
<summary>Django 管理者作成手順</summary>
    
Djangoでの管理者作成は、以下のコマンドで行う。  
```
docker compose exec web python manage.py createsuperuser
```  
もしくは  
```
make csu
```  
コマンド入力後に、ユーザー名、メールアドレス（省略可）、パスワードが聞かれるため、各自で設定する。  
ブラウザに以下のアドレスを入力し、設定したユーザー名とパスワードを入力し、ログインできるか確認する。  
```
http://localhost:8000/ or http://127.0.0.1:8000/
```  
成功すると以下の画面が表示される。  
<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/db0ab465-c744-4f87-8bbd-0e018c0beaa2" />
</details>

<br>

## インフラ設計の詳細
以降より、自身が担当したインフラ設計の詳細を述べる。

<details>
<summary>1. 作業フロー</summary>
次のとおり、本インフラ設計の作業フローを示す。
</details>

<details>
<summary>2. ディレクトリ・ファイル構成の検討</summary>
</details>

<details>
<summary>3. インフラ技術の選定</summary>
</details>

<details>
<summary>4. Dockerによる開発環境構築</summary>
</details>

<details>
<summary>5. AWSインフラ構成図の検討</summary>

**1)インフラ構成図**

**2)技術選定理由**

</details>

<details>
<summary>6. AWS環境構築</summary>
</details>

<details>
<summary>7. 本番環境へのデプロイ</summary>
</details>








