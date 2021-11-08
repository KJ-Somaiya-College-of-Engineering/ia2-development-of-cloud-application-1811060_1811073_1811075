import baseUrl from "./baseUrl";

export default async function(context) {
    const token = context.$store.getters.getAuthToken;
    context.$axios.setHeader('token', token);
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$get(
      `${baseUrl}/url`
    );
    if(response.STATUS == "OK") return response.DATA;
  }
  