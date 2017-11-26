require 'sinatra'
require 'json'


get '/' do
   send_file 'index.html'
end

post '/image' do
  file = Base64.decode64(params[:image].split(',')[1])
  path = "./uploaded/#{SecureRandom.hex}.png"
  
  File.open(path, 'wb') do |f|
    f.write(file)
  end

  predictions = JSON.parse(`python predict.py #{path}`)
  return predictions ? "Face not found" : predictions
end
