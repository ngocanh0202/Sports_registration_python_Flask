let input = document.getElementById("search_name");
input.addEventListener('input', async function(){
    let respone = await fetch("/tool_search?name="+input.value)
    let list_name = await respone.text();
    document.querySelector("ul").innerHTML = list_name
});