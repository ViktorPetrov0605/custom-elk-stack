# Chapter: A Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_01.html
**Type:** Configuration Commands - Navigation/Index

## Content Summary

```
if (typeof cdc === "undefined"){
 cdc = {};
 }
 cdc.localizedLang="en/us";

 if (window.cdcext === undefined) { window.cdcext = {}; }
 cdcext.customEnvironment = "prod";
 if (window.cdclocale === undefined) { window.cdclocale = {}; }
 cdclocale.locale = cdc.localizedLang=="en/us"?"en_us":cdc.localizedLang;

 window['adrum-start-time'] = new Date().getTime();
 window.environ = "prod" ;

 if (window.cpe === undefined) {
 window.cpe = {};
 }

 cpe.accountName = "prod";
 cpe.config = ["cinf","dsc","pps"];
 cpe.hideMethod = "elements";

 window.targetGlobalSettings = JSON.parse('{\x22timeout\x22:4000}');
 window.targetPageParamsAll = () => JSON.parse('{\x22entity\x22:\x22{\\\x22id\\\x22:\\\x221563691850911921\\\x22,\\\x22categoryId\\\x22:\\\x22\\\x22}\x22}');

 const bullseyeLibrary = `/etc.clientlibs/cisco-cdc/clientlibs/clientlib-external/resources/external/bullseye.js`;

 import(bullseyeLibrary);

 Cisco Nexus 9000 Series NX-OS Command Reference (Configuration Commands), Release 9.3(x) - A Commands [Cisco Nexus 9000 Series Switches] - Cisco

 $CQ(function() {
 CQ_Analytics.SegmentMgr.loadSegments("\/etc\/segmentation");
 CQ_Analytics.ClientContextUtils.init("\/c\/dnc\/etc\/clientcontext\/default", "\/content\/en\/us\/td\/docs\/switches\/datacenter\/nexus9000\/sw\/93x\/command\/reference\/config\/b_N9K_Config_Commands_93x\/b_N9K_Config_Commands_93x_chapter_01");

 });

 sessionStorage.setItem("logOutIntermediateMessage", 'You are being logged out.');

 [

 {
 "@context": "http:/
```

## Document Structure

This file contains navigation and reference material for the Cisco Nexus 9000 NX-OS Command Reference.

---

**Note:** Original navigation file processed. Contains 283 links to other sections.
