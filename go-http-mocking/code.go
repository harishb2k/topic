"github.com/jarcoal/httpmock"
"github.com/stretchr/testify/assert"


type AutoGenerated struct {
    UserID    int    `json:"userId"`
    ID        int    `json:"id"`
    Title     string `json:"title"`
    Completed bool   `json:"completed"`
}

httpmock.Activate()
defer httpmock.DeactivateAndReset()


// Setup - setup a response to HTTP call
s := `{
            "userId": 1,
            "id": 1,
            "title": "a",
            "completed": false
    }`

obj := server.AutoGenerated{}
if err := json.Unmarshal([]byte(data), &obj); err != nil {
	panic(err)
}

httpmock.RegisterResponder("GET", "https://jsonplaceholder.typicode.com/todos/1",
    func(req *http.Request) (*http.Response, error) {
        resp, err := httpmock.NewJsonResponse(200, obj)
        if err != nil {
            return httpmock.NewStringResponse(500, ""), nil
        }
        return resp, nil
    },
)

// Real call - Call your code which calls to http endpoint
// R is the data returened from server
r := MyCall() 

assert.Equal(t, 1, r.ID, "Id must be 1")
assert.Equal(t, 200, code, "code must 200")


// you can verify if yoy did call HTTP
info := httpmock.GetCallCountInfo()
assert.Equal(t, 0, info["GET https://api.mybiz.com/articles"], "Id must be 1")

