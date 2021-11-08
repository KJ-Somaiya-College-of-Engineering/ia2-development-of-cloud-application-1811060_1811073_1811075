import baseUrl from "./baseUrl";

export default async function (token, context) {
    if(!token) return;
    const resp = await context.$axios.$get(`${baseUrl}/auth/verify?token=${token}`, { progress: true })
    console.log(resp)
    if(resp.STATUS == "OK"){
        return resp.DATA;
    }
}