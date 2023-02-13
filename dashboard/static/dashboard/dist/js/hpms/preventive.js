moment.locale('fr');
const site_id = JSON.parse(document.getElementById('site_id').textContent); 
const week = JSON.parse(document.getElementById('week').textContent); 
const year = JSON.parse(document.getElementById('year').textContent); 
first_day=moment().isoWeekYear(year).isoWeek(week).day('Lundi')
console.log(first_day)
last_day= moment(first_day).add(6, 'days')
e= document.getElementById('tbody_planning')
var url = $("#tbody_planning").attr("data-url");  

fetch(url)
.then((resp) => resp.json())
.then(function(data){
  tr1=document.createElement('tr')
  td0=document.createElement('td')
  td0.setAttribute('class','bg-light')
  td0.setAttribute('style','5%')
  td0.innerHTML=''
  tr1.appendChild(td0)
  td1=document.createElement('td')
  td1.setAttribute('class','bg-light')
  td1.setAttribute('style','30%')
  td1.innerHTML='Désignation'
  tr1.appendChild(td1)
  td2=document.createElement('td')
  td2.setAttribute('class','bg-light')
  td2.setAttribute('style','15%')
  td2.innerHTML='Zone'
  tr1.appendChild(td2)  
  td3=document.createElement('td')
  td3.setAttribute('class','bg-light')
  td3.setAttribute('style','15%')
  td3.innerHTML='Equipement'
  tr1.appendChild(td3)
  for(let i=0;i<=6;i++){
  day= moment(first_day).add(i,'days')
  day=moment(day).local().format('ddd DD/MM')
  td4=document.createElement('td')
  td4.setAttribute('style','border:1px solid;border-color:#EBECF0;')
  td4.innerHTML=day
  tr1.appendChild(td4)
  }
  e.appendChild(tr1)
  for (let i=0; i< data['planifications'].length ; i++){
    var cc=''
    if(data['planifications'][i]['periodicite'] == 'Hebdomadaire'){
      cc='bg-success text-white'
    }else if(data['planifications'][i]['periodicite'] == 'Mensuelle'){
      cc='bg-warning text-white'
    }else if(data['planifications'][i]['periodicite'] == 'Trimestrielle'){
      cc='bg-info text-white'
    }else if(data['planifications'][i]['periodicite'] == 'Semestrielle'){
      cc='bg-primary text-white'
    }else if(data['planifications'][i]['periodicite'] == 'Annuelle'){
      cc='bg-secondary text-white'
    }
    tr = document.createElement('tr')
    td0=document.createElement('td')
    a1=document.createElement('a')
    url1=`preventive/x/modifier`.replace('x',data['planifications'][i]['id']);
    a1.setAttribute('href',url1)
    a1.setAttribute('class','text-decoration-none text-dark')
    a1.innerHTML='<i class="ti-pencil"></i>'
    td0.appendChild(a1)
    tr.appendChild(td0)
    td1=document.createElement('td')
    td1.innerHTML=data['planifications'][i]['objet']
    tr.appendChild(td1)    
    td2=document.createElement('td')
    td2.innerHTML=data['planifications'][i]['zone']
    tr.appendChild(td2)    
    td3=document.createElement('td')
    td3.innerHTML=data['planifications'][i]['equipement']
    tr.appendChild(td3)
    for (let t=0;t<=6;t++){    
      day= moment(first_day).add(t, 'days')
      day=moment(day).local().format('YYYY-MM-DD')
      td =document.createElement('td')
      td.setAttribute('style','border:1px solid;border-color:#EBECF0;')
      for (let j=0; j<data['planifications'][i]['interventions'].length; j++){
        intervention_day=data['planifications'][i]['interventions'][j]['datecharge']
        intervention_day=moment(intervention_day).local().format('YYYY-MM-DD')
        if (intervention_day == day){
          url=`preventive/intervention/x`.replace('x',data['planifications'][i]['interventions'][j]['id']);
          td.setAttribute('class',cc)
          a=document.createElement('a')
          a.setAttribute('href',url)
          a.setAttribute('class','text-decoration-none text-white')
          a.innerHTML='<i class="ti-info-alt"></i>'
          td.appendChild(a)
        }
      }
      tr.appendChild(td)
    }   
    e.appendChild(tr)
  }
})