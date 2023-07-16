import yfinance as yf # 야후 파이낸스에서 가져오는 주식 정보
import datetime
import plotly.graph_objects as go # 그래프 전용 모듈
import streamlit as st

st.write("# 주식차트")

# ticker = "TSLA"
ticker = st.text_input("종목코드 입력 >> ") # 스트림릿 인풋함수
# 한국 주식은 뒤에 .KS 붙여야함
data = yf.Ticker(ticker)
# datetime :
# datetime.datetime.today() 오늘 날짜 불러오기
# datetime.datetime.today().strftime("%Y-%m-%d %H -%M -%S")
today = datetime.datetime.today().strftime("%Y-%m-%d")
# period : 1d 데이터를 가져올 날짜 간격
df = data.history(period="1d", start="2015-01-01", end=today)
# print(df)
st.write(df)

# 그래프 그리기
# df 설명 바깥쪽은 인덱싱 연산자 # 안쪽은 리스트 연산자
st.line_chart(df[["Close", "High"]])
st.bar_chart(df["Volume"])

# plotly 이용 그래프 만들기
candle = go.Candlestick(
    x=df.index,
    high=df["High"], low=df["Low"],
    open=df["Open"], close=df["Close"]
)
layout = go.Layout(yaxis={"fixedrange": False}) #y축의 고정된 레인지를 해제시켜주는 것
fig = go.Figure(data=[candle], layout=layout)
# fig.show() # 화면에 띄우는
st.plotly_chart(fig)
