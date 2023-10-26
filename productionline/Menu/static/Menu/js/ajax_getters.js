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
            end:enddate
        },
        dataType: 'json',
        success: function (data) {
            
            console.log(data);
            
            var table = document.querySelector('.table-striped tbody');

            
            table.innerHTML = '';

            var rowNum = 1;
            console.log("ENTERING THE FUNCTION");
            
            for (const product in data) {
                if (data.hasOwnProperty(product)) {
                    const rowData = data[product];
                    var row = document.createElement('tr');

                    var th = document.createElement('th');
                    th.setAttribute('scope', 'row');
                    th.textContent = rowNum;
                    row.appendChild(th);

                    var btn = document.createElement('button');
                    btn.style.margin = "10px";
                    btn.style.width = "10px";
                    btn.style.height = "10px";
                    btn.style.color = "white";
                    btn.style.backgroundColor = "red";
                    btn.innerHTML = "Bad";

                    
                    rowData.forEach(function (value) {
                        

                        var td = document.createElement('td');
                        console.log("VALUE:" + value);
                        if(value == "true"){
                            btn.backgroundColor = "green";
                            btn.innerHTML = "Good";
                            td.appendChild(btn);
                        }else if(value == "false"){
                            td.appendChild(btn);
                        }else{
                            td.textContent = value;
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