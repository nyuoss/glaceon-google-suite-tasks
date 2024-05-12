// JavaScript to toggle the dropdown
function toggleDropdown(detailId) {
    var element = document.getElementById(detailId);
    if (element) {
        element.classList.toggle('show');
    }
}

function search_task(id) {
    let input = document.getElementById(id).value.toLowerCase();
  console.log(input);
    let tasklists = document.getElementsByClassName("category");
    for (i=0; i<tasklists.length; i++){
        if (tasklists[i].innerHTML.toLowerCase().includes(input)) {
            console.log(tasklists[i]);
            tasklists[i].style.display = "list-item";
        } else {
            console.log(tasklists[i]);
            tasklists[i].style.display = "none";
        }
    }
}ƒ
