import baseUrl from "./baseUrl";

export default async function(email, context) {
  context.$axios.setHeader('Content-Type', 'application/json')
  const response = await context.$axios.$post(
    `${baseUrl}/authenticate`,
    {
      email: email
  });
  if (response.STATUS == "OK") return true;
}
