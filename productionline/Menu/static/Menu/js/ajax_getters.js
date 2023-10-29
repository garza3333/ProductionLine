$(document).ready(function () {
    var plantSelect = $('#plantSelect');
    var lineSelect = $('#lineSelect');

    plantSelect.on('change', function () {
        var selectedplantname = plantSelect.val();
        console.log(selectedplantname);

        $.ajax({
            url: '/getlinesnames/'+selectedplantname,
            type: 'GET',
            data: {
                plant_id: selectedplantname 
            },
            dataType: 'json',
            success: function (data) {
          
                lineSelect.empty();
                console.log(data);

                var firstoption = document.createElement('option');
                firstoption.value = 'Select Line';
                firstoption.text = 'Select Line';
                lineSelect.append(firstoption);

               
                $.each(data, function (key, value) {

                    
                    lineSelect.append($('<option>', {
                        value: value,
                        text: value
                    }));
                });
            },
            error: function (error) {
                console.error('Error from AJAX:', error);
            }
        });
    });
});


function searchbottles(){

    console.log("searching bottles");
    console.log("searching bottles");

    var plantname = $('#plantSelect').val();
    var linename = $('#lineSelect').val();

    // date format: 2023-10-26 12:00
    var begindate = document.getElementById("initdatepicker").value;
    var enddate = document.getElementById("endddatepicker").value;

    console.log(plantname);
    console.log(linename);
    console.log(begindate);
    console.log(enddate);


    
    $.ajax({
        url: '/getlinesdata/'+linename,
        type: 'GET',
        data: {
            beg:begindate,
            end:enddate,
            pplant: plantname
        },
        dataType: 'json',
        success: function (data) {
            
            console.log(data);
            
            var table = document.querySelector('.table-striped tbody');

            
            table.innerHTML = '';

            var rowNum = 1;
            
            
            for (const product in data) {
                if (data.hasOwnProperty(product)) {
                    const rowData = data[product];
                    var row = document.createElement('tr');

                    var th = document.createElement('th');
                    th.setAttribute('scope', 'row');
                    th.textContent = rowNum;
                    row.appendChild(th);

                    var btnb = document.createElement('button');
                    btnb.innerHTML = "Bad";
                    btnb.classList.add("btnb");

                    var btng = document.createElement('button');
                    btng.innerHTML = "Good";
                    btng.classList.add("btng");
                 
                    
                    
                    rowData.forEach(function (value) {

                        var td = document.createElement('td');
                        
                        if(value == true){
                            td.appendChild(btng);
                        }else if(value == false){
                            td.appendChild(btnb);
                        }else{
                            td.textContent = value;
                            td.style.textAlign = "center";
                        }
                        
                        
                        row.appendChild(td);
                    });

                    table.appendChild(row);
                    rowNum++;
                }
            }
        },
        error: function (error) {
            console.error('Error from AJAX:', error);
        }
    });

}