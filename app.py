import gradio as gr
import socket
def do(url):
  outp=socket.gethostbyname(url)
  return outp
iface=gr.Interface(fn=do,title='網站ip找尋工具',description='輸入一個網址，我們可以幫您找到他的ip.',inputs='text',outputs='text')
iface.launch(share=True)