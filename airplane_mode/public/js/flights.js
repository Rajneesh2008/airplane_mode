
let search_btn = document.querySelector(".search-flight-btn")

search_btn.addEventListener("click",()=>{

    let source_city = document.querySelector(".source_city").value
    let destination_city = document.querySelector(".destination_city").value
    let departure = document.querySelector(".departure_date").value
    
    let url = new  URLSearchParams()

    if(source_city && destination_city){
        url.append("source_city",source_city)
        url.append("destination_city",destination_city)
    }
    if(source_city && destination_city && departure){
        url.append("departure",departure)
    }

  window.location.href =  source_city && destination_city ? `${window.location.pathname}?${url.toString()}`:`${window.location.pathname}`
})