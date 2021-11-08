import baseUrl from "./baseUrl";

export default async function(urlid, context) {
  const token = context.$store.state.authToken;
  context.$axios.setHeader('token', token);
  context.$axios.setHeader('Content-Type', 'application/json')
  const response = await context.$axios.$delete(`${baseUrl}/url?urlid=${urlid}`);
  if (response.STATUS == "OK") return true;
  return false;
}