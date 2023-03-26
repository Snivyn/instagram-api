import axios from "axios"

export async function getUserContent(username: string, ctx: object): Promise<object>{
    return (await axios.get(`https://www.instagram.com/api/v1/users/web_profile_info/?username=${username}`, { headers: ctx })).data
}