import streamlit as st
from lunar＿python import Solar
from google import genai

st.set_page_config(page_title="紫微斗數 × 中醫經絡智慧排盤系統", layout="centered")

st.title("🌟 紫微斗數 × 中醫經絡智慧排盤系統")
st.markdown("輸入你的出生國曆時間，即時解析經絡氣機、宮位與病理命盤，並透過 AI 進行整體臨床合參！")

# 輸入介面
col1, col2, col3 = st.columns(3)
with col1:
    year = st.number_input("出生年份 (西元)", value=2000, step=1)
with col2:
    month = st.number_input("出生月份", value=1, min_value=1, max_value=12, step=1)
with col3:
    day = st.number_input("出生日期", value=1, min_value=1, max_value=31, step=1)

col4, col5 = st.columns(2)
with col4:
    hour = st.number_input("出生小時 (24小時制)", value=6, min_value=0, max_value=23, step=1)
with col5:
    minute = st.number_input("出生分鐘", value=0, min_value=0, max_value=59, step=1)

if st.button("✨ 開始排盤與解析", type="primary"):
    try:
        solar = Solar.fromYmdHms(int(year), int(month), int(day), int(hour), int(minute), 0)
        lunar = solar.getLunar()
        
        st.success("排盤計算成功！")
        
        # 1. 基礎陣列與變數定義
        branches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        lunar_month = abs(lunar.getMonth())  
        time_zhi = lunar.getTimeZhi()       
        birth_time_index = branches.index(time_zhi) + 1

        # 2. 繁體中文顯示基本資訊
        lunar_year_cn = lunar.getYearInChinese()
        lunar_month_cn = lunar.getMonthInChinese()
        lunar_day_cn = lunar.getDayInChinese()
        
        st.subheader("【基本曆法與干支資訊】")
        st.write(f"**國曆時間**：{year}年{month}月{day}日 {hour:02d}:{minute:02d}")
        st.write(f"**農曆日期**：{lunar_year_cn}年{lunar_month_cn}{lunar_day_cn} {time_zhi}時")
        st.write(f"**四柱干支**：{lunar.getYearInGanZhi()}年 | {lunar.getMonthInGanZhi()}月 | {lunar.getDayInGanZhi()}日 | {lunar.getTimeInGanZhi()}時")

        # 3. 字典資料庫
        branch_to_organ = {
            '子': '子宮 (足少陽膽經)', '丑': '丑宮 (足厥陰肝經)', '寅': '寅宮 (手太陰肺經)',
            '卯': '卯宮 (手陽明大腸經)', '辰': '辰宮 (足陽明胃經)', '巳': '巳宮 (足太陰脾經)',
            '午': '午宮 (手少陰心經)', '未': '未宮 (手太陽小腸經)', '申': '申宮 (足太陽膀胱經)',
            '酉': '酉宮 (足少陰腎經)', '戌': '戌宮 (手厥陰心包經)', '亥': '亥宮 (手少陽三焦經)'
        }

        tcm_star_descriptions = {
            '紫微': '脾胃中焦土樞，主統攝與領導 (思慮過重易脾虛濕阻)',
            '天機': '膽經、神經與四肢，主靈動思維 (氣機易升發過度致肝風失眠)',
            '太陽': '心、小腸與面部，主光明溫煦 (心神易亢，過旺則心火上炎)',
            '武曲': '肺、大腸與筋骨，主肅降剛毅 (氣機收斂過猛致胸悶筋骨僵硬)',
            '天同': '水道、三焦與津液，主溫潤福氣 (失調易生痰濕水飲代謝遲緩)',
            '廉貞': '心包絡與血分，主血熱剛烈 (心神易悶塞化火，自律神經失調)',
            '天府': '胃、三焦與蓄積能力，主庫櫝涵容 (過度沉積易腹脹痰濕肥胖)',
            '太陰': '腎水、陰血與內分泌，主月亮滋潤 (不足易虛勞失眠血虛)',
            '貪狼': '肝膽、生殖泌尿與筋膜，主欲望升發 (擾動時易口苦筋膜緊繃)',
            '巨門': '口腔、呼吸道黏膜與腎水，主口舌水飲 (氣道津液易阻滯、咽喉不利)',
            '天相': '膀胱、三焦與水分調節，主印星協調 (失調易水液代謝失職水腫)',
            '天梁': '脾土、肌肉與免疫修復，主壽星庇蔭 (自癒力強，帶有濕濁沈重)',
            '七殺': '肺與應激防衛系統，主肅殺將星 (交感神經高張，處於急性發炎)',
            '破軍': '腎與大腸（代謝循環），主耗散劇烈變動 (能量劇烈消耗，過度則元氣大傷)',
            '擎羊': '【煞】針刺樣痛感、外傷、氣滯血瘀',
            '陀羅': '【煞】慢性隱痛、糾纏不清的阻滯、濕瘀互結',
            '火星': '【煞】熱邪、燥火、急性發炎',
            '鈴星': '【煞】熱邪、燥火、隱性燥發',
            '地空': '【煞】氣陷、虛空、能量漏失',
            '地劫': '【煞】氣陷、虛空、吸收不良',
            '祿存': '【吉】精氣充盈、固本培元',
            '天馬': '【吉】氣血運行、動態流轉',
            '左輔': '【吉】脾土之氣輔助',
            '右弼': '【吉】腎水之陰涵化',
            '文昌': '【吉】金氣、思維條理',
            '文曲': '【吉】水氣、情感與津液代謝',
            '天魁': '【吉】陽貴人、升發之氣',
            '天鉞': '【吉】陰貴人、深層修復'
        }

        # 4. 命身宮計算
        yin_index = 2
        month_stop_index = (yin_index + (lunar_month - 1)) % 12
        life_palace_index = (month_stop_index - (birth_time_index - 1)) % 12
        body_palace_index = (life_palace_index + (birth_time_index - 1)) % 12

        palace_names = ['命宮', '兄弟宮', '夫妻宮', '子女宮', '財帛宮', '疾厄宮', '遷移宮', '交友宮', '官祿宮', '田宅宮', '福德宮', '父母宮']
        palace_map = {}
        for i, palace in enumerate(palace_names):
            current_index = (life_palace_index - i) % 12
            branch_name = branches[current_index]
            if branch_name not in palace_map:
                palace_map[branch_name] = []
            palace_map[branch_name].append(palace)

        # 5. 五行局與星曜計算
        heavenly_stems = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        year_gan = lunar.getYearInGanZhi()[0]
        tiger_start_gan = {'甲': '丙', '己': '丙', '乙': '戊', '庚': '戊', '丙': '庚', '辛': '庚', '丁': '壬', '壬': '壬', '戊': '甲', '癸': '甲'}
        start_gan = tiger_start_gan.get(year_gan)
        start_gan_index = heavenly_stems.index(start_gan)
        steps_from_yin = (life_palace_index - yin_index) % 12
        life_palace_gan_index = (start_gan_index + steps_from_yin) % 10
        life_palace_gan = heavenly_stems[life_palace_gan_index]
        life_palace_ganzhi = life_palace_gan + branches[life_palace_index]

        def get_nayin_bureau(ganzhi_str):
            wood_zu_jue = ['甲子', '乙丑', '戊辰', '己巳', '庚寅', '辛卯', '壬午', '癸未', '庚申', '辛酉', '戊戌', '己亥']
            water_zu_jue = ['丙子', '丁丑', '甲寅', '乙卯', '壬辰', '癸巳', '丙午', '丁未', '甲申', '乙酉', '戊子', '己丑']
            metal_zu_jue = ['壬申', '癸酉', '庚辰', '辛巳', '甲午', '乙未', '壬寅', '癸卯', '庚戌', '辛亥', '丙辰', '丁巳']
            earth_zu_jue = ['丙辰', '丁巳', '庚午', '辛未', '戊申', '己酉', '丙戌', '丁亥', '庚子', '辛丑', '戊寅', '己卯']
            if ganzhi_str in wood_zu_jue: return "木三局", 3
            elif ganzhi_str in water_zu_jue: return "水二局", 2
            elif ganzhi_str in metal_zu_jue: return "金四局", 4
            elif ganzhi_str in earth_zu_jue: return "土五局", 5
            else: return "火六局", 6

        bureau_name, bureau_number = get_nayin_bureau(life_palace_ganzhi)
        lunar_day = lunar.getDay()
        bureau_num = bureau_number

        remainder = lunar_day % bureau_num
        if remainder == 0:
            ziwei_index = (yin_index + ((lunar_day // bureau_num) - 1)) % 12
        else:
            complement = bureau_num - remainder
            adjusted_day = lunar_day + complement
            quotient = adjusted_day // bureau_num
            if complement % 2 != 0:
                ziwei_index = (yin_index + (quotient - 1) - complement) % 12
            else:
                ziwei_index = (yin_index + (quotient - 1) + complement) % 12

        tianfu_index = (4 - ziwei_index) % 12

        ziwei_group = [('紫微', 0), ('天機', -1), ('太陽', -3), ('武曲', -4), ('天同', -5), ('廉貞', -8)]
        tianfu_group = [('天府', 0), ('太陰', 1), ('貪狼', 2), ('巨門', 3), ('天相', 4), ('天梁', 5), ('七殺', 6), ('破軍', 8)]

        star_map = {i: [] for i in range(12)}
        for star_name, offset in ziwei_group:
            star_map[(ziwei_index + offset) % 12].append(star_name)
        for star_name, offset in tianfu_group:
            star_map[(tianfu_index + offset) % 12].append(star_name)

        # 輔佐煞曜
        star_map[(3 + (lunar_month - 1)) % 12].append('左輔')
        star_map[(9 - (lunar_month - 1)) % 12].append('右弼')
        star_map[(9 - (birth_time_index - 1)) % 12].append('文昌')
        star_map[(3 + (birth_time_index - 1)) % 12].append('文曲')

        tiankui_tianyue_map = {
            '甲': (1, 7), '戊': (1, 7), '庚': (1, 7), '乙': (0, 8), '己': (0, 8),
            '丙': (11, 9), '丁': (11, 9), '壬': (3, 5), '癸': (3, 5), '辛': (6, 2)
        }
        kui, yue = tiankui_tianyue_map.get(year_gan, (1, 7))
        star_map[kui].append('天魁')
        star_map[yue].append('天鉞')

        lucun_map = {'甲': 2, '乙': 3, '丙': 5, '丁': 6, '戊': 5, '己': 6, '庚': 8, '辛': 9, '壬': 11, '癸': 0}
        lucun_pos = lucun_map.get(year_gan, 2)
        star_map[lucun_pos].append('祿存')
        star_map[(lucun_pos + 1) % 12].append('擎羊')
        star_map[(lucun_pos - 1) % 12].append('陀羅')

        year_zhi = lunar.getYearInGanZhi()[1]
        hx_start = {'寅': 1, '午': 1, '戌': 1, '申': 2, '子': 2, '辰': 2, '巳': 3, '酉': 3, '丑': 3, '亥': 9, '卯': 9, '未': 9}.get(year_zhi, 1)
        lx_start = {'寅': 3, '午': 3, '戌': 3, '申': 10, '子': 10, '辰': 10, '巳': 11, '酉': 11, '丑': 11, '亥': 10, '卯': 10, '未': 10}.get(year_zhi, 3)
        star_map[(hx_start + (birth_time_index - 1)) % 12].append('火星')
        star_map[(lx_start + (birth_time_index - 1)) % 12].append('鈴星')

        star_map[(11 - (birth_time_index - 1)) % 12].append('地空')
        star_map[(11 + (birth_time_index - 1)) % 12].append('地劫')

        # 四化
        birth_hua = {
            '甲': ('廉貞', '破軍', '武曲', '太陽'), '乙': ('天機', '天梁', '紫微', '太陰'),
            '丙': ('天同', '天機', '文昌', '廉貞'), '丁': ('太陰', '天同', '天機', '巨門'),
            '戊': ('貪狼', '太陰', '右弼', '天機'), '己': ('武曲', '貪狼', '天梁', '文曲'),
            '庚': ('太陽', '武曲', '太陰', '天同'), '辛': ('巨門', '太陽', '文曲', '文昌'),
            '壬': ('天梁', '紫微', '左輔', '天機'), '癸': ('破軍', '巨門', '太陰', '貪狼')
        }
        lu, quan, ke, ji = birth_hua.get(year_gan, ('', '', '', ''))

        for pos in star_map:
            updated_stars = []
            for star in star_map[pos]:
                if star == lu: updated_stars.append(f"{star}【化祿】")
                elif star == quan: updated_stars.append(f"{star}【化權】")
                elif star == ke: updated_stars.append(f"{star}【化科】")
                elif star == ji: updated_stars.append(f"{star}【化忌】")
                else: updated_stars.append(star)
            star_map[pos] = updated_stars

        st.subheader(f"【五行局】：{bureau_name} (生年干：{year_gan})")

        # 6. 網頁呈現結果
        chart_summary = []
        for i, branch in enumerate(branches):
            palaces = palace_map.get(branch, [])
            palace_str = ', '.join(palaces) if palaces else "（無主宮）"
            stars = star_map.get(i, [])
            
            tags = []
            if i == life_palace_index: tags.append("★ 命宮")
            if i == body_palace_index: tags.append("◆ 身宮")
            tag_str = f"  [{' '.join(tags)}]" if tags else ""
            
            organ_str = branch_to_organ.get(branch, branch)
            
            star_details = []
            with st.expander(f"【{organ_str}】 {palace_str} {tag_str}"):
                if stars:
                    for star in stars:
                        clean_star = star.split('【')[0]
                        desc = tcm_star_descriptions.get(clean_star, '經絡氣機流轉位點')
                        st.markdown(f"- **{star}**：{desc}")
                        star_details.append(f"{star}：{desc}")
                else:
                    st.markdown("- *（本經絡無主星與主要煞曜駐守，氣機平和）*")
                    star_details.append("本經絡平和，無主星與主要煞曜")

            chart_summary.append(f"【{organ_str}】宮位屬性: {palace_str}{tag_str} | 駐守星曜與病理: {', '.join(star_details)}")

        # ==========================================
        # 7. AI 智慧中醫經絡命理整體解讀
        # ==========================================
        st.markdown("---")
        st.subheader("🤖 AI 智慧中醫經絡命理整體解讀")
        user_question = st.text_input("你想特別請教 AI 什麼方向？", value="請針對這張經絡命盤進行整體身心氣機與體質傾向的深度綜合分析")

        if st.button("🔮 請 AI 進行臨床中醫經絡綜合解讀", type="primary"):
            with st.spinner("AI 正在結合紫微星象與中醫經絡學理，為您深度解析中..."):
                full_chart_text = "\n".join(chart_summary)
                prompt = f"""
                你是一位融合了「傳統紫微斗數象數推演」與「中醫學理、經絡氣機、身心病機」的頂尖中醫師與命理專家。
                現在有一位使用者的紫微斗數經絡命盤數據如下：
                
                【基本生辰】
                生年干支：{year_gan}年 | 五行局：{bureau_name}
                命宮位置：{branches[life_palace_index]}宮 | 身宮位置：{branches[body_palace_index]}宮
                
                【十二經絡與星曜病理分佈】
                {full_chart_text}
                
                【使用者的提問或關注點】
                {user_question}
                
                請根據以上數據，以專業、溫暖且具臨床洞察力的語氣，提供一份結構化的整體解讀報告，包含：
                1. **先天體質與氣機樞紐分析**（結合命身宮與五行局的整體氣血特質）。
                2. **核心病理與經絡卡點**（特別指出受煞曜或化忌影響、容易出現功能失調的經絡與臟腑）。
                3. **身心互動與潛在傾向**（星曜象數如何對應到情緒、壓力模式或生理表現）。
                4. **日常中醫養生與調理建議**（飲食、作息、情志調節等具體方向）。
                
                請使用繁體中文回答，排版清晰易讀。
                """

                api_key = st.secrets["GEMINI_API_KEY"]
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )

                st.success("分析完成！")
                st.markdown("### 📋 AI 臨床中醫經絡命理綜合報告")
                st.markdown(response.text)

    except Exception as e:
        st.error(f"計算過程發生錯誤或 API Key 未正確設定：{e}")

