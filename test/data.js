/*fetch("tanks_data.json")

.then(function(response){
    return response.json();
})

.then (function(tanks_data){
    let placeholder = document.querySelector('#data-output');

    let out = "";

    for (let tank of tanks_data){
        out+= `
        <tr>
            <td>${tank.name}</td>
            <td>${tank.nation}</td>
            <td>${tank.battle_rating}</td>
            <td>${tank.type}</td>
        </tr>
        `;
    }
    placeholder.innerHTML = out;
})
*/


/*function fetchJSONData(){
    fetch('./tanks_data.json').then((res) =>{
        if (!res.ok){
            throw new Error
                ('HTTP error! Status: ${res.status}');
        }
        return res.json();
    })
    
    .then((data) =>
        console.log(data))
    .catch((error)=>
            console.error("Unable to fetch data:", error));
    }
    
    fetchJSONData();

*/
const mysql = require('mysql2');

// create a new MySQL connection
const connection = mysql.createConnection({
  host: '127.0.0.1',
  port : 3306,
  user: 'root',
  password: 'Shorty051699@',
  database: 'War_Thunder_API'
});
// connect to the MySQL database
connection.connect((error) => {
  if (error) {
    console.error('Error connecting to MySQL database:', error);
  } else {
    console.log('Connected to MySQL database!');
  }
});

// close the MySQL connection
connection.end();