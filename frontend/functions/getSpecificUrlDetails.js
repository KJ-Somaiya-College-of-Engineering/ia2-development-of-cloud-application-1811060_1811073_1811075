import baseUrl from "./baseUrl";

export default async function (urlid, context) {
    const token = context.getAuthToken;
    context.$axios.setHeader('token', token);
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$get(
      `${baseUrl}/url/details?id=${urlid}`
    );
    if(response.STATUS == "OK") {
        return response.DATA
    }
}