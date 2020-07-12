


type AutoGenerated struct {
    UserID    int    `json:"userId"`
    ID        int    `json:"id"`
    Title     string `json:"title"`
    Completed bool   `json:"completed"`
}

output := AutoGenerated{}
resp, _ := http.Get(url)
defer resp.Body.Close()

body, _ := ioutil.ReadAll(resp.Body)
if err := json.Unmarshal(body, &output); err != nil {
    panic(err)
}