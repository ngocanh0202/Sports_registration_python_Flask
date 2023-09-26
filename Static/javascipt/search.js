let input = document.getElementById("search_name");
input.addEventListener('input', async function(){
    let respone = await fetch("/tool_search?name="+input.value)
    let list_name = await respone.json();
    let html = ""
    for(let a in list_name){
        html += "<li>"+list_name[a][0]+"</li>"
    }
    document.querySelector("ul").innerHTML = html
});