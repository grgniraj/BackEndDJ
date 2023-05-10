fetch("http://localhost:8000/api/products/")
  .then((response) => response.json())
  .then((data) => {
    document.getElementById("totalproducts").innerHTML = data.length;
  })
  .catch((error) => {
    console.error("Error:", error);
  });

fetch("http://localhost:8000/api/users/")
  .then((response) => response.json())
  .then((data) => {
    document.getElementById("totalusers").innerHTML = data.length;
  })
  .catch((error) => {
    console.error("Error:", error);
  });

fetch("http://localhost:8000/api/orders/")
  .then((response) => response.json())
  .then((data) => {
    document.getElementById("totalorders").innerHTML = data.length;
  })
  .catch((error) => {
    console.error("Error:", error);
  });
