
async function submit() {

    let msg=document.getElementById("confirmationText1").value;
    let data = {"text": msg};
    let res = await (fetch("http://localhost:8000", {
    method: "POST",
    headers:{'Content-Type': 'application/json'},
    body:JSON.stringify(data)
    
  }))
  let resul=await res.json();
  document.getElementById("confirmationText2").value=resul.result;
  document.getElementById("beforep").innerHTML=resul.before;


}