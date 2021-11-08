import baseUrl from "./baseUrl";

export default async function(url, context) {
  const token = context.$store.state.authToken;
  context.$axios.setHeader('token', token);
  context.$axios.setHeader('Content-Type', 'application/json')
  const response = await context.$axios.$post(
    `${baseUrl}/url`,
    {
      redirect: url
  });
  if (response.STATUS == "OK") return { ID: response.ID, OG_DETAILS: response.OG_DETAILS };
}
