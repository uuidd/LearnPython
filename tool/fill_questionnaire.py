#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !@Author:liyihui
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from fake_useragent import UserAgent
from random import choice


async def click_options():
    for _ in range(100):
        # browser = await launch(headless=False, executablePath=r"C:\Usersoftware\Chrome 78.0.3904.108\App\chrome.exe")
        browser = await launch(headless=False)
        page = await browser.newPage()
        await page.setUserAgent(UserAgent().random)
        await stealth(page)
        await page.goto("https://www.wjx.cn/vm/PMJrFNk.aspx")  # 问卷地址
        await page.evaluate(
            '''async () =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
        # 寻找答案位置，触发点击操作
        await query_click(page, '[for="q1_{0}"]'.format(await three_num()))
        await query_click(page, '[for="q2_{0}"]'.format(await three_num()))
        await query_click(page, '[for="q3_{0}"]'.format(await four_num()))
        await query_click(page, '[for="q4_{0}"]'.format(await two_num()))
        await query_click(page, '[for="q5_{0}"]'.format(await three_num()))
        await query_click(page, '[for="q6_{0}"]'.format(await two_num()))
        await query_click(page, '[for="q7_{0}"]'.format(await three_num()))
        await query_click(page, '[for="q8_{0}"]'.format(await three_num()))
        await query_click(page, '[for="q9_{0}"]'.format(await four_num()))
        await query_click(page, '[for="q10_{0}"]'.format(await four_num()))
        await page.evaluate('_ => {window.scrollBy(0, window.innerHeight);}')
        await asyncio.sleep(2)
        await query_click(page, '[id="ctlNext"]')  # 触发提交按钮
        await asyncio.sleep(2)
        # await page.close()
        await browser.close()  # 关闭浏览器


# 点击指定答案
async def query_click(page, element):
    submit = await page.querySelector(element)
    await submit.click()


async def two_num():
    return choice([1, 1, 1, 1, 1, 1, 1, 2, 2])


async def three_num():
    return choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3])


async def four_num():
    return choice([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])


async def main():
    await asyncio.gather(
        click_options()
    )

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    # asyncio.run(main())
