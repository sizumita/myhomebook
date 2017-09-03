/**
 * Created by sizumita on 2017/09/02.
 */
function getJSON() {
  var req = new XMLHttpRequest();		  // XMLHttpRequest オブジェクトを生成する
  req.onreadystatechange = function() {		  // XMLHttpRequest オブジェクトの状態が変化した際に呼び出されるイベントハンドラ
    if(req.readyState == 4 && req.status == 200){ // サーバーからのレスポンスが完了し、かつ、通信が正常に終了した場合
      alert(req.responseText);		          // 取得した JSON ファイルの中身を表示
    }
  };
  req.open("GET", "https://www.googleapis.com/books/v1/volumes?q=あ", false); // HTTPメソッドとアクセスするサーバーの　URL　を指定
  req.send(null);					    // 実際にサーバーへリクエストを送信
}