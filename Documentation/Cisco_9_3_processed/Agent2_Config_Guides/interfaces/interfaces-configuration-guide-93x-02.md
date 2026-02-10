# Cisco Nexus 9000 シリーズ NX-OS インターフェイス設定ガイド、リリース 9.3(x)

**Source:** `b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_02.html`
**Tags:** interfaces, ethernet, port-channels, switchport

---

Cisco Nexus 9000 シリーズ NX-OS インターフェイス設定ガイド、リリース 9.3(x) - Cisco 	 	 
 
- [#fw-content] Skip to Main content 
- [#] 検索にジャンプ 
- [#fw-footer-v2] Skip to Footer 

- [https://www.cisco.com/site/jp/ja/index.html] 
- [/c/ja_jp/products/index.html] 
- [https://www.cisco.com/site/jp/ja/solutions/index.html] 
- [/c/ja_jp/support/index.html] 
- [/c/ja_jp/training-events.html] 
- [/c/ja_jp/about/sitemap.html] 
- [/c/ja_jp/buy.html] 
- [https://www.cisco.com/site/jp/ja/partners/index.html] 
- [/c/ja_jp/partners/partner-with-cisco.html?ccid=cc000864&dtid=odiprc001129] 
- [https://www.cisco.com/site/jp/ja/partners/support-help/index.html] 
- [/c/ja_jp/partners/tools.html] 
- [https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/] 
- [https://www.cisco.com/site/jp/ja/partners/connect-with-a-partner/index.html] 
- [https://www.cisco.com/site/jp/ja/partners/index.html] 	 

- [#] 
- [/c/ja_jp/support/index.html] 
- [/c/ja_jp/support/all-products.html] 
- [/c/ja_jp/support/switches/category.html] 
- [/c/ja_jp/support/switches/nexus-9000-series-switches/series.html] 
- [/c/ja_jp/support/switches/nexus-9000-series-switches/products-installation-and-configuration-guides-list.html] 		 
# Cisco Nexus 9000 シリーズ NX-OS インターフェイス設定ガイド、リリース 9.3(x)
 		 	 偏向のない言語 翻訳について 
### 偏向のない言語
 

この製品のドキュメントセットは、偏向のない言語を使用するように配慮されています。このドキュメントセットでの偏向のない言語とは、年齢、障害、性別、人種的アイデンティティ、民族的アイデンティティ、性的指向、社会経済的地位、およびインターセクショナリティに基づく差別を意味しない言語として定義されています。製品ソフトウェアのユーザインターフェイスにハードコードされている言語、RFP のドキュメントに基づいて使用されている言語、または参照されているサードパーティ製品で使用されている言語によりドキュメントに例外が存在する場合があります。シスコのインクルーシブ ランゲージの取り組みの詳細は、[https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html] こちらをご覧ください。
 
### 翻訳について
 

このドキュメントは、米国シスコ発行ドキュメントの参考和訳です。リンク情報につきましては、日本語版掲載時点で、英語版にアップデートがあり、リンク先のページが移動/変更されている場合がありますことをご了承ください。あくまでも参考和訳となりますので、正式な内容については米国サイトのドキュメントを参照ください。
 Search このマニュアル内で検索 保存 [/c/login/index.html?referer=/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.html] ログインしてコンテンツを保存 [https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.html] 英語 ご利用いただける言語 
 ダウンロード Download Options 
### 

 
 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.pdf] PDF - Complete Book (6.07 MB) 

View with Adobe Reader on a variety of devices
 プリント 
## 検索結果
 Updated: 2025年7月14日月曜日 
## マニュアルの目次
 
 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_preface_00.html] はじめに 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01.html] 新機能と変更情報 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010.html] 概要 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01110.html] 基本インターフェイス パラメータの設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0100.html] レイヤ 2 インターフェイスの設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_0101.html] レイヤ 3 インターフェイスの設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01111.html] 双方向フォワーディング検出の設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_010000.html] ポート チャネルの構成 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01000.html] vPC の設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01001.html] IP トンネルの設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01010.html] Q-in-Q VLAN トンネルの設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01011.html] スタティックおよびダイナミック NAT 変換の設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01100.html] IP イベント減衰の設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_chapter_01101.html] IP TCP MSS の設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/m-n9000-configuring-unidirectional-ethernet.html] 単一方向イーサネットの設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_appendix_01110.html] レイヤ 2 Data Center Interconnect の設定 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_appendix_01111.html] Cisco NX-OS インターフェイスがサポートする IETF RFC 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_appendix_010000.html] Cisco NX-OS インターフェイスの設定制限 
- [/c/ja_jp/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x_index.html] Index 
### Notes
 
### 

### 

- [https://mycase.cloudapps.cisco.com/start?prodDocUrl=] 
- [//www.cisco.com/c/ja_jp/services/order-services.html] 
### 

- [/c/ja_jp/support/switches/nexus-9000-series-switches/series.html]
