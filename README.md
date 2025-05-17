# X Auto Poster - Standalone Version

このアプリはローカル環境で X（旧 Twitter）に毎日決まった時間に自動投稿するスタンドアローン型システムです。
OS：WSL2 + Ubuntu 22.04.3 LTS

## 機能

- 複数アカウント対応
- 投稿時刻と内容の設定
- Python スクリプトによる自動投稿

## 使用技術

- Python 3.10.12
- Tweepy==4.14.0（Twitter API ラッパー）
- schedule==1.2.0（簡易スケジューラ）
- 今回は AOuth1.0a だからユーザ認証いらない

## ディレクトリ構成

```md
.
├── main.py # メインスクリプト（投稿処理＋スケジューラ）
├── accounts.json # 各 X アカウントの情報と投稿設定（.gitignore 対象）
├── README.md
└── .gitignore # Git 管理除外設定
```

## セットアップ方法

1. https://developer.twitter.com/en/ にアクセスし`accounts.json` を作成＆保存

2. OAuth 1.0a 設定。「Projects & Apps」＞「Standalone Apps」タブ＞「＋ Create App」

- Authentication Type: OAuth 1.0a
- App permissions: Read and Write
- Callback URL: http://localhost（手動認証なので何でも OK）
- Website URL (required)：GitHub の URL にした（なんでも Ok）
- 以下は保存必須（再表示なし）
- API Key（Consumer Key）：アプリ識別
- API Secret Key（Consumer Secret）
  ※「OAuth 2.0 Client ID and Client Secret」は今回は使わないため、保存の必要は無し

3. 投稿操作を許可

- 「App settings」＞「App permissions」＞ App permissions を Read and Write
  ※「Save」したら、Access Token の再生成！！

4. 各種キーの取得（「Keys and Tokens」タブ＞「Generate Access Token and Secret」）

- API Key（Consumer Key）：アプリ識別
- API Secret Key（Consumer Secret）
- Access Token：ユーザ認証
- Access Token Secret
  ※再表示ないのでテキスト保存必須。

5. 必要ライブラリをインストール：

   ```bash
   pip install tweepy schedule
   ```

6. メッセージを json ファイルへ追加（下記の例参照）

7. 実行：
   `bash
python main.py
`
   ※プログラム実行中の動作する

## accounts.json 例

```json
[
  {
    "id": "account1",
    "access_token": "...",
    "access_token_secret": "...",
    "api_key": "...",
    "api_secret": "...",
    "post_time": "09:00",
    "message": "おはようございます！"
  }
]
```

## 推奨運用（パソコンを起動していれば自動実行）

### Windows:タスクスケジューラ登録手順
1. Windowsキー > 「タスクスケジューラ」
2. 「基本タスクの作成」
- 名前：X Auto Poster
- 説明：起動時にXへ投稿を行うBot
3. トリガーを選択
- 「コンピュータの起動時」または「ログオン時」
4. 操作の選択
- プログラム：python
- 引数："C:\your\path\to\main.py"
5. 完了後、右クリックで「プロパティ」
- 「条件」タブで「電源に関係なく実行」などを調整
※main.py → main.pyw にすれば、ウィンドウ非表示になります（GUIなし）

## 投稿機能の制限について

２０２４年以降投稿制限により有料出ないと投稿の機能は使えなくなっている。

### 選択肢

- selenium で疑似投稿（非公式）
- basic プラン（100$/月）へグレードアップして、投稿機能（v1.1 の POST statuses/update）を使えるようにする。
