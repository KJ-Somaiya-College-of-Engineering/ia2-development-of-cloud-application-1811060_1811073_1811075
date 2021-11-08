import baseUrl from "./baseUrl";

export default async function(name, email, context) {
  context.$axios.setHeader('Content-Type', 'application/json')
  const response = await context.$axios.$post(
    `${baseUrl}/auth/new`,
    {
      email: email,
      name: name
  });
  if (response.STATUS == "OK") return true;
}
