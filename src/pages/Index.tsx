import { ChatInterface } from '@/components/chat/ChatInterface';

const Index = () => {
  return (
    <div className="h-screen">
      <ChatInterface apiEndpoint="YOUR_BACKEND_ENDPOINT_HERE" />
    </div>
  );
};

export default Index;
