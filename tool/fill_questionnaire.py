#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# !@Author:liyihui
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
# from fake_useragent import UserAgent
from random import choice

# 问卷网址
URL = "https://www.wjx.cn/vm/PMJrFNk.aspx"
# 按顺序题目对应的答案数
answer = [3, 3, 4, 2, 3, 2, 3, 3, 4, 4]


async def click_options():
    browser = await launch({'headless': False})
    for _ in range(100):
        page = await browser.newPage()
        # 反爬虫
        await stealth(page)
        # 问卷地址
        await page.goto(URL)
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
        await page.evaluate("""{window.scrollBy(0, document.body.scrollHeight);}""")
        await asyncio.sleep(2)
        # 提交
        await query_click(page, '[id="ctlNext"]')
        await asyncio.sleep(2)
        # 判断是否有出现智能检测
        if await page.querySelector('[id="SM_TXT_1"]'):
            await browser.close()
            browser = await launch({'headless': False})
            print("提交失败！")
        else:
            await page.close()
            await asyncio.sleep(3)
            print("提交成功！")


async def find_ele():
    for i in range(len(answer)):
        for j in range(i):
            return '[for="q{0}_{1}"]'.format(i, j)


# 点击单选框
async def click_single_choice(page, element):
    ele = await page.querySelector(element)
    await ele.click()


# 点击指定答案
async def query_click(page, element):
    ele = await page.querySelector(element)
    await ele.click()
    await page.evaluate('_ => {window.scrollBy(0, window.innerHeight);}')


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
