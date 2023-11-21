import gradio as gr
from pipeline_1 import content_pipeline
from pipeline_2 import ad_pipeline
from flagging import ResultLogger
from Llama_chatbot import chat


strategy_options = ['Festive Promotion', 'Event-specific advertisement', 'Educational-use highlight', 'Educational-use highlight','Tech versatility showcase','Seasonal refresh']
domain_options = ['Problem solution', 'Storytelling narrative']
context_options = ['Utilize information','Ensure accuracy','Refer to','Incorporate','Leverage']

custom_callback = ResultLogger(folder_path="logs/")
marketing_prompt = gr.Interface(
    fn=content_pipeline,
    inputs=[
        gr.components.Textbox(lines=2, placeholder="Enter initial prompt here..."),
        gr.components.Dropdown(choices=strategy_options, label="Strategy"),
        gr.components.Dropdown(choices=domain_options, label="Domain"),
        gr.components.Dropdown(choices=context_options,label="context"),
      

    ],
    outputs=gr.components.Textbox(lines=10, placeholder="Generated text will appear here..."),
    title="Generate Marketing Content",
    description="Select options to generate marketing content."
)

ad_display_creatives = gr.Interface(
    fn=ad_pipeline,
    inputs=[
        gr.components.Textbox(lines=2, placeholder="Enter the prompt generated from previous step..")
        ],
    outputs =[gr.components.Textbox(lines=10),gr.Gallery(label="generated Images", elem_id="gallery",columns=[2],rows=[4],object_fit="contain",height="auto")],
    title="Display ad and image banners",
    flagging_options=["I like it! 👍", "Nah..! 👎"],
    flagging_dir="ad_logs",
    flagging_callback=custom_callback
    
)

chatbot = gr.ChatInterface(fn=chat)

demo = gr.TabbedInterface(
    interface_list=[marketing_prompt,ad_display_creatives,chatbot],
    tab_names=["generate marketing content","display ad and image banners","LLama Powered Chatbot"]
)
demo.launch()

