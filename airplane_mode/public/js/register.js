
let formData = document.getElementById("register");

formData.addEventListener("submit",(e)=>{
    e.preventDefault();
    
    const fullName = document.querySelector(".fullName").value;
    const email = document.querySelector(".email").value;
    const password = document.querySelector(".password").value;

   fetch("/api/method/airplane_mode.api.register",{
        method:"POST",
        headers:{
            "content-type":"application/json",
            "X-Frappe-CSRF-Token":document.querySelector("#csrf").value || "",
        },
        body:JSON.stringify({email,password,fullName})

    })
    .then((res)=>{
        alert("You have recevied an email for verification please click on verify link.")
       return res.json()
    })
    
    .then((data)=>{
        if(data?.status == "Success"){
            alert(data?.msg)
            console.log(data)
        }
    }).catch((error)=>{
        console.log(error)
    })
})