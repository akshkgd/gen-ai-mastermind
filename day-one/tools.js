import OpenAI from "openai";
import 'dotenv/config'
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-4.1-mini",
    tools: [
        { type: "web_search" },
    ],
    input: "3 most important news headlines from india??",
});

console.log(response.output_text);