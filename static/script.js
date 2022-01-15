function makePost(content){

  var url = "/api/newpost";
  
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url);
  
  xhr.setRequestHeader("Content-Type", "application/json");
  
  xhr.onreadystatechange = function () {
     if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
        if (xhr.status == 200){
          window.location.reload();
        } else{
          alert("Error "+xhr.status);
          location.href = "/error/"+xhr.status;
        }
     }};
  
  var data = '{"content":"'+content+'"}';
  
  xhr.send(data);

}
