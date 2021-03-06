// Django REST Framework url
const drf = 'http://localhost:8000/apiv1/users/';


// API
const api = async (url) => {
  const res = await fetch(url);
  // json
  const users = await res.json();
  console.log(users);
}


// run
const res = api(drf);
