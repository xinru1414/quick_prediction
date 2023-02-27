function say_hello() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "name": document.getElementById('name').value
    });

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/hello", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('respond_text').innerText = result)
    .catch(error => console.log('error', error));
}
