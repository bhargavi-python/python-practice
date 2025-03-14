from playwright.sync_api import sync_playwright, Page


class TraceViewer:

    def __init__(self, page: Page):
        self.page = page

    def traceviewer(self, page):

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            context.tracing.start(
                screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            page.goto("https://www.google.com")

            context.tracing.stop(path="trace.zip")
            context.close()
