var likes = [9, 12, 9];
var comment = 
[document.querySelector("#comment-1")
,document.querySelector("#comment-2")
,document.querySelector("#comment-3")];


function like(id){
likes[id]++;
comment[id].innerHTML = likes[id] + " like(s)";
}