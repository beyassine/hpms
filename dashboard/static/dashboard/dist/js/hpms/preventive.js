
const site_id = JSON.parse(document.getElementById('site_id').textContent); 
const month = JSON.parse(document.getElementById('month').textContent); 
e= document.getElementById('tbody_planning')

var url = $("#tbody_planning").attr("data-url");  

function n(n){
  return n > 9 ? "" + n: "0" + n;
}

fetch(url)
.then((resp) => resp.json())
.then(function(data){
  dm=moment(month, "YYYY-MM-DD").daysInMonth() 
  tr1=document.createElement('tr')
  td1=document.createElement('td')
  td1.setAttribute('class','bg-light')
  td1.innerHTML='Désignation'
  tr1.appendChild(td1)
  for(let d=1;d<=dm;d++){
  td2=document.createElement('td')
  td2.innerHTML=n(d)
  tr1.appendChild(td2)
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
    td=document.createElement('td')
    td.setAttribute('class','bg-light')
    a1=document.createElement('a')
    url1=`preventive/x/modifier`.replace('x',data['planifications'][i]['id']);
    a1.setAttribute('href',url1)
    a1.setAttribute('class','text-decoration-none text-dark')
    a1.innerHTML=data['planifications'][i]['objet']
    td.appendChild(a1)
    tr.appendChild(td)
    for (let t=1;t<=dm;t++){
      td =document.createElement('td')
      td.setAttribute('styke','width:5px;')
      for (let j=0; j<data['planifications'][i]['interventions'].length; j++){
        var dtd=moment(data['planifications'][i]['interventions'][j]['datecharge']).format('D');
        var dtm=moment(data['planifications'][i]['interventions'][j]['datecharge']).format('M');
        if (dtd == t){
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