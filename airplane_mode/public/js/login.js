let form =  document.querySelector("#login-form")
console.log(form)

form.addEventListener("submit",(e)=>{
    e.preventDefault();
    
    const email = document.querySelector(".email").value
    const password = document.querySelector(".password").value

    fetch("/api/method/airplane_mode.api.login",{
        method:"POST",
        headers:{
            "content-type":"application/json",
            'X-Frappe-CSRF-Token': document.querySelector("#csrf").value||""
        },
        body:JSON.stringify({email,password})
    }).then((data)=>{
        if(data.status==200){
            console.log("Logged In")
            window.location.href = `/home`
        }else{
            console.log(data)
        }
    }).catch((err)=>{
        console.log(err)
    })

})