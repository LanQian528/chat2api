import base64
import hashlib
import json
import random
import time
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser

from utils.Logger import logger

cores = [16, 24, 32]
screens = [3000, 4000, 6000]
timeLayout = "%a %b %d %Y %H:%M:%S"

cached_scripts = []
cached_dpl = ""
cached_time = 0
cached_require_proof = ""

navigator_key = ['hardwareConcurrency−16', 'login−[object NavigatorLogin]']
document_key = ['_reactListeningpa877jnmig', 'location']
window_key = [
    "0",
    "window",
    "self",
    "document",
    "name",
    "location",
    "customElements",
    "history",
    "navigation",
    "locationbar",
    "menubar",
    "personalbar",
    "scrollbars",
    "statusbar",
    "toolbar",
    "status",
    "closed",
    "frames",
    "length",
    "top",
    "opener",
    "parent",
    "frameElement",
    "navigator",
    "origin",
    "external",
    "screen",
    "innerWidth",
    "innerHeight",
    "scrollX",
    "pageXOffset",
    "scrollY",
    "pageYOffset",
    "visualViewport",
    "screenX",
    "screenY",
    "outerWidth",
    "outerHeight",
    "devicePixelRatio",
    "clientInformation",
    "screenLeft",
    "screenTop",
    "styleMedia",
    "onsearch",
    "isSecureContext",
    "trustedTypes",
    "performance",
    "onappinstalled",
    "onbeforeinstallprompt",
    "crypto",
    "indexedDB",
    "sessionStorage",
    "localStorage",
    "onbeforexrselect",
    "onabort",
    "onbeforeinput",
    "onbeforematch",
    "onbeforetoggle",
    "onblur",
    "oncancel",
    "oncanplay",
    "oncanplaythrough",
    "onchange",
    "onclick",
    "onclose",
    "oncontentvisibilityautostatechange",
    "oncontextlost",
    "oncontextmenu",
    "oncontextrestored",
    "oncuechange",
    "ondblclick",
    "ondrag",
    "ondragend",
    "ondragenter",
    "ondragleave",
    "ondragover",
    "ondragstart",
    "ondrop",
    "ondurationchange",
    "onemptied",
    "onended",
    "onerror",
    "onfocus",
    "onformdata",
    "oninput",
    "oninvalid",
    "onkeydown",
    "onkeypress",
    "onkeyup",
    "onload",
    "onloadeddata",
    "onloadedmetadata",
    "onloadstart",
    "onmousedown",
    "onmouseenter",
    "onmouseleave",
    "onmousemove",
    "onmouseout",
    "onmouseover",
    "onmouseup",
    "onmousewheel",
    "onpause",
    "onplay",
    "onplaying",
    "onprogress",
    "onratechange",
    "onreset",
    "onresize",
    "onscroll",
    "onsecuritypolicyviolation",
    "onseeked",
    "onseeking",
    "onselect",
    "onslotchange",
    "onstalled",
    "onsubmit",
    "onsuspend",
    "ontimeupdate",
    "ontoggle",
    "onvolumechange",
    "onwaiting",
    "onwebkitanimationend",
    "onwebkitanimationiteration",
    "onwebkitanimationstart",
    "onwebkittransitionend",
    "onwheel",
    "onauxclick",
    "ongotpointercapture",
    "onlostpointercapture",
    "onpointerdown",
    "onpointermove",
    "onpointerrawupdate",
    "onpointerup",
    "onpointercancel",
    "onpointerover",
    "onpointerout",
    "onpointerenter",
    "onpointerleave",
    "onselectstart",
    "onselectionchange",
    "onanimationend",
    "onanimationiteration",
    "onanimationstart",
    "ontransitionrun",
    "ontransitionstart",
    "ontransitionend",
    "ontransitioncancel",
    "onafterprint",
    "onbeforeprint",
    "onbeforeunload",
    "onhashchange",
    "onlanguagechange",
    "onmessage",
    "onmessageerror",
    "onoffline",
    "ononline",
    "onpagehide",
    "onpageshow",
    "onpopstate",
    "onrejectionhandled",
    "onstorage",
    "onunhandledrejection",
    "onunload",
    "crossOriginIsolated",
    "scheduler",
    "alert",
    "atob",
    "blur",
    "btoa",
    "cancelAnimationFrame",
    "cancelIdleCallback",
    "captureEvents",
    "clearInterval",
    "clearTimeout",
    "close",
    "confirm",
    "createImageBitmap",
    "fetch",
    "find",
    "focus",
    "getComputedStyle",
    "getSelection",
    "matchMedia",
    "moveBy",
    "moveTo",
    "open",
    "postMessage",
    "print",
    "prompt",
    "queueMicrotask",
    "releaseEvents",
    "reportError",
    "requestAnimationFrame",
    "requestIdleCallback",
    "resizeBy",
    "resizeTo",
    "scroll",
    "scrollBy",
    "scrollTo",
    "setInterval",
    "setTimeout",
    "stop",
    "structuredClone",
    "webkitCancelAnimationFrame",
    "webkitRequestAnimationFrame",
    "chrome",
    "caches",
    "cookieStore",
    "ondevicemotion",
    "ondeviceorientation",
    "ondeviceorientationabsolute",
    "launchQueue",
    "documentPictureInPicture",
    "getScreenDetails",
    "queryLocalFonts",
    "showDirectoryPicker",
    "showOpenFilePicker",
    "showSaveFilePicker",
    "originAgentCluster",
    "onpageswap",
    "onpagereveal",
    "credentialless",
    "speechSynthesis",
    "onscrollend",
    "webkitRequestFileSystem",
    "webkitResolveLocalFileSystemURL",
    "sendMsgToSolverCS",
    "webpackChunk_N_E",
    "__next_set_public_path__",
    "next",
    "__NEXT_DATA__",
    "__SSG_MANIFEST_CB",
    "__NEXT_P",
    "_N_E",
    "regeneratorRuntime",
    "__REACT_INTL_CONTEXT__",
    "DD_RUM",
    "_",
    "filterCSS",
    "filterXSS",
    "__SEGMENT_INSPECTOR__",
    "__NEXT_PRELOADREADY",
    "Intercom",
    "__MIDDLEWARE_MATCHERS",
    "__STATSIG_SDK__",
    "__STATSIG_JS_SDK__",
    "__STATSIG_RERENDER_OVERRIDE__",
    "_oaiHandleSessionExpired",
    "__BUILD_MANIFEST",
    "__SSG_MANIFEST",
    "__intercomAssignLocation",
    "__intercomReloadLocation"
]


class ScriptSrcParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global cached_scripts, cached_dpl, cached_time
        if tag == "script":
            attrs_dict = dict(attrs)
            if "src" in attrs_dict:
                src = attrs_dict["src"]
                cached_scripts.append(src)
                if "dpl" in src:
                    cached_dpl = src[src.index("dpl"):]
                    cached_time = int(time.time())


async def get_dpl(service):
    global cached_scripts, cached_dpl, cached_time
    if int(time.time()) - cached_time < 15 * 60:
        return True
    headers = service.base_headers.copy()
    try:
        r = await service.s.get(f"{service.host_url}/?oai-dm=1", headers=headers)
        r.raise_for_status()
        parser = ScriptSrcParser()
        parser.feed(r.text)
        if len(cached_scripts) == 0:
            cached_scripts.append("https://cdn.oaistatic.com/_next/static/cXh69klOLzS0Gy2joLDRS/_ssgManifest.js?dpl=453ebaec0d44c2decab71692e1bfe39be35a24b3")
            cached_dpl = "453ebaec0d44c2decab71692e1bfe39be35a24b3"
            cached_time = int(time.time())
        return True
    except Exception:
        return False


def get_parse_time():
    now = datetime.now(timezone(timedelta(hours=+9)))
    return now.strftime(timeLayout) + " GMT+0900 (Japan Standard Time)"


def get_config(user_agent):
    core = random.choice(cores)
    screen = random.choice(screens)
    config = [
        core + screen,
        get_parse_time(),
        4294705152,
        0,
        user_agent,
        random.choice(cached_scripts) if len(cached_scripts) > 0 else None,
        cached_dpl,
        "en-US",
        "en-US,en",
        0,
        random.choice(navigator_key),
        random.choice(document_key),
        random.choice(window_key)
    ]
    return config


def get_answer_token(seed, diff, config):
    start = time.time()
    answer = generate_answer(seed, diff, config)
    end = time.time()
    logger.info(f'seed: {seed}, diff: {diff}, time: {int((end - start) * 1e6) / 1e3}ms')
    return "gAAAAAB" + answer


def generate_answer(seed, diff, config):
    diff_len = len(diff)
    seed_encoded = seed.encode()

    for i in range(500000):
        config[3] = i
        config[9] = i
        json_data = json.dumps(config, separators=(',', ':'), ensure_ascii=False)
        base = base64.b64encode(json_data.encode()).decode()
        hasher = hashlib.sha3_512()
        hasher.update(seed_encoded + base.encode())
        hash_value = hasher.digest()
        if hash_value.hex()[:diff_len] <= diff:
            return base

    return "wQ8Lk5FbGpA2NcR9dShT6gYjU7VxZ4D" + base64.b64encode(f'"{seed}"'.encode()).decode()


def get_requirements_token(config):
    require_token = generate_answer(format(random.random()), "0", config)
    return 'gAAAAAC' + require_token
