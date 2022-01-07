function makePost(author, content){

  var url = "https://Backslash.theh4ck3r.repl.co/api/newpost";
  
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url);
  
  xhr.setRequestHeader("Content-Type", "application/json");
  
  xhr.onreadystatechange = function () {
     if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
       window.location.reload()
     }};
  
  var data = '{"author": "'+author+'", "content":"'+content+'"}';
  
  xhr.send(data);

}

